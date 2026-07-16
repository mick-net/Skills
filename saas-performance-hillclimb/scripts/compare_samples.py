#!/usr/bin/env python3
"""Compare repeated baseline and candidate performance samples."""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from numbers import Real
from pathlib import Path
from typing import Iterable


SUMMARY_STATISTICS = ("min", "max", "mean", "median", "p90", "p95", "p99")


def _normalize_samples(samples: Iterable[Real]) -> tuple[float, ...]:
    try:
        values = tuple(samples)
    except TypeError as error:
        raise ValueError("samples must be an iterable of numeric values") from error

    if len(values) < 2:
        raise ValueError("samples must contain at least two values")

    normalized = []
    for value in values:
        if isinstance(value, bool) or not isinstance(value, Real):
            raise ValueError("sample values must be numeric and not boolean")
        converted = float(value)
        if not math.isfinite(converted):
            raise ValueError("sample values must be finite")
        normalized.append(converted)
    return tuple(normalized)


@dataclass(frozen=True)
class SampleSet:
    """An immutable set of repeated measurements for one metric."""

    metric: str
    unit: str
    direction: str
    samples: tuple[float, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.metric, str) or not self.metric.strip():
            raise ValueError("metric must be a non-empty string")
        if not isinstance(self.unit, str) or not self.unit.strip():
            raise ValueError("unit must be a non-empty string")
        if self.direction not in ("lower", "higher"):
            raise ValueError("direction must be 'lower' or 'higher'")
        object.__setattr__(self, "samples", _normalize_samples(self.samples))


def load_sample_set(path: str | Path) -> SampleSet:
    """Load and validate a sample set from a JSON file."""

    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("sample file must contain a JSON object")

    required = {"metric", "unit", "direction", "samples"}
    missing = sorted(required - set(payload))
    unexpected = sorted(set(payload) - required)
    schema_errors = []
    if missing:
        schema_errors.append(f"missing fields: {', '.join(missing)}")
    if unexpected:
        schema_errors.append(f"unexpected fields: {', '.join(unexpected)}")
    if schema_errors:
        raise ValueError(f"sample file schema mismatch: {'; '.join(schema_errors)}")
    if not isinstance(payload["samples"], list):
        raise ValueError("samples must be a JSON list")

    return SampleSet(
        metric=payload["metric"],
        unit=payload["unit"],
        direction=payload["direction"],
        samples=tuple(payload["samples"]),
    )


def _percentile(sorted_samples: tuple[float, ...], percentile: float) -> float:
    position = (len(sorted_samples) - 1) * percentile
    lower_index = math.floor(position)
    upper_index = math.ceil(position)
    if lower_index == upper_index:
        return sorted_samples[lower_index]
    weight = position - lower_index
    return (
        sorted_samples[lower_index] * (1.0 - weight)
        + sorted_samples[upper_index] * weight
    )


def summarize(samples: Iterable[Real]) -> dict[str, float | int]:
    """Summarize finite samples with linear-interpolated percentiles."""

    values = tuple(sorted(_normalize_samples(samples)))
    return {
        "count": len(values),
        "min": values[0],
        "max": values[-1],
        "mean": math.fsum(values) / len(values),
        "median": _percentile(values, 0.5),
        "p90": _percentile(values, 0.9),
        "p95": _percentile(values, 0.95),
        "p99": _percentile(values, 0.99),
    }


def compare(baseline: SampleSet, candidate: SampleSet) -> dict:
    """Compare matching sample sets and report direction-aware improvements."""

    baseline_metadata = (baseline.metric, baseline.unit, baseline.direction)
    candidate_metadata = (candidate.metric, candidate.unit, candidate.direction)
    if baseline_metadata != candidate_metadata:
        raise ValueError("baseline and candidate metadata must match")

    baseline_summary = summarize(baseline.samples)
    candidate_summary = summarize(candidate.samples)
    deltas = {}
    for statistic in SUMMARY_STATISTICS:
        baseline_value = float(baseline_summary[statistic])
        candidate_value = float(candidate_summary[statistic])
        absolute = candidate_value - baseline_value
        if baseline_value == 0:
            percent = None
            improvement = None
        else:
            percent = absolute / baseline_value * 100.0
            directional_delta = -absolute if baseline.direction == "lower" else absolute
            improvement = directional_delta / abs(baseline_value) * 100.0
        deltas[statistic] = {
            "absolute": absolute,
            "percent": percent,
            "improvement_percent": improvement,
        }

    return {
        "metric": baseline.metric,
        "unit": baseline.unit,
        "direction": baseline.direction,
        "baseline": baseline_summary,
        "candidate": candidate_summary,
        "deltas": deltas,
    }


def _format_number(value: float | int | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def _format_text(result: dict) -> str:
    lines = [
        f"{result['metric']} ({result['unit']}; {result['direction']} is better)"
    ]
    for statistic in SUMMARY_STATISTICS:
        delta = result["deltas"][statistic]
        lines.append(
            f"{statistic}: baseline={_format_number(result['baseline'][statistic])} "
            f"candidate={_format_number(result['candidate'][statistic])} "
            f"delta={_format_number(delta['absolute'])} "
            f"improvement={_format_number(delta['improvement_percent'])}%"
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Compare repeated baseline and candidate performance samples."
    )
    parser.add_argument("baseline", help="Path to the baseline JSON file")
    parser.add_argument("candidate", help="Path to the candidate JSON file")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)

    try:
        result = compare(
            load_sample_set(args.baseline),
            load_sample_set(args.candidate),
        )
    except (OSError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))

    if args.format == "json":
        print(json.dumps(result, indent=2, sort_keys=True, allow_nan=False))
    else:
        print(_format_text(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
