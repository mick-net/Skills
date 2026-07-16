import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from compare_samples import SampleSet, compare, load_sample_set, summarize


class CompareSamplesTests(unittest.TestCase):
    def test_lower_is_better_reports_positive_improvement(self):
        baseline = SampleSet("latency", "ms", "lower", (100.0, 120.0, 140.0, 160.0))
        candidate = SampleSet("latency", "ms", "lower", (80.0, 90.0, 100.0, 110.0))

        result = compare(baseline, candidate)

        self.assertGreater(result["deltas"]["median"]["improvement_percent"], 0)

    def test_higher_is_better_reports_positive_improvement(self):
        baseline = SampleSet("throughput", "rps", "higher", (10.0, 12.0, 14.0))
        candidate = SampleSet("throughput", "rps", "higher", (15.0, 17.0, 19.0))

        result = compare(baseline, candidate)

        self.assertGreater(result["deltas"]["median"]["improvement_percent"], 0)

    def test_lower_is_better_handles_negative_baseline(self):
        baseline = SampleSet("offset", "ms", "lower", (-10.0, -10.0))
        candidate = SampleSet("offset", "ms", "lower", (-20.0, -20.0))

        result = compare(baseline, candidate)

        self.assertEqual(
            100.0,
            result["deltas"]["median"]["improvement_percent"],
        )

    def test_higher_is_better_handles_negative_baseline(self):
        baseline = SampleSet("offset", "ms", "higher", (-20.0, -20.0))
        candidate = SampleSet("offset", "ms", "higher", (-10.0, -10.0))

        result = compare(baseline, candidate)

        self.assertEqual(
            50.0,
            result["deltas"]["median"]["improvement_percent"],
        )

    def test_rejects_non_finite_or_too_few_samples(self):
        with self.assertRaisesRegex(ValueError, "finite"):
            SampleSet("latency", "ms", "lower", (1.0, float("nan")))
        with self.assertRaisesRegex(ValueError, "at least two"):
            SampleSet("latency", "ms", "lower", (1.0,))

    def test_rejects_mismatched_metadata(self):
        baseline = SampleSet("latency", "ms", "lower", (100.0, 120.0))
        candidate = SampleSet("throughput", "rps", "higher", (10.0, 12.0))

        with self.assertRaisesRegex(ValueError, "metadata"):
            compare(baseline, candidate)

    def test_summarize_uses_linear_interpolated_percentiles(self):
        result = summarize((10.0, 20.0, 30.0, 40.0))

        self.assertEqual(4, result["count"])
        self.assertEqual(10.0, result["min"])
        self.assertEqual(40.0, result["max"])
        self.assertEqual(25.0, result["mean"])
        self.assertEqual(25.0, result["median"])
        self.assertAlmostEqual(37.0, result["p90"])
        self.assertAlmostEqual(38.5, result["p95"])
        self.assertAlmostEqual(39.7, result["p99"])

    def test_rejects_boolean_samples(self):
        with self.assertRaisesRegex(ValueError, "numeric"):
            SampleSet("latency", "ms", "lower", (1.0, True))

    def test_zero_baseline_statistic_has_no_percentage_delta(self):
        baseline = SampleSet("offset", "ms", "lower", (0.0, 0.0))
        candidate = SampleSet("offset", "ms", "lower", (-1.0, 1.0))

        result = compare(baseline, candidate)

        self.assertIsNone(result["deltas"]["median"]["percent"])
        self.assertIsNone(result["deltas"]["median"]["improvement_percent"])

    def test_load_sample_set_parses_json_object(self):
        with tempfile.TemporaryDirectory() as directory:
            sample_path = Path(directory, "samples.json")
            sample_path.write_text(
                json.dumps(
                    {
                        "metric": "latency",
                        "unit": "ms",
                        "direction": "lower",
                        "samples": [100, 120],
                    }
                )
            )

            result = load_sample_set(sample_path)

            self.assertEqual(
                SampleSet("latency", "ms", "lower", (100.0, 120.0)),
                result,
            )

    def test_load_sample_set_rejects_unexpected_field(self):
        with tempfile.TemporaryDirectory() as directory:
            sample_path = Path(directory, "samples.json")
            sample_path.write_text(
                json.dumps(
                    {
                        "metric": "latency",
                        "unit": "ms",
                        "direction": "lower",
                        "samples": [100, 120],
                        "typo": True,
                    }
                )
            )

            with self.assertRaisesRegex(ValueError, "unexpected fields: typo"):
                load_sample_set(sample_path)

    def test_cli_rejects_unexpected_field(self):
        with tempfile.TemporaryDirectory() as directory:
            baseline_path = Path(directory, "baseline.json")
            candidate_path = Path(directory, "candidate.json")
            baseline_path.write_text(
                json.dumps(
                    {
                        "metric": "latency",
                        "unit": "ms",
                        "direction": "lower",
                        "samples": [100, 120],
                        "typo": True,
                    }
                )
            )
            candidate_path.write_text(
                json.dumps(
                    {
                        "metric": "latency",
                        "unit": "ms",
                        "direction": "lower",
                        "samples": [80, 90],
                    }
                )
            )

            completed = subprocess.run(
                [
                    sys.executable,
                    str(Path(__file__).with_name("compare_samples.py")),
                    str(baseline_path),
                    str(candidate_path),
                    "--format",
                    "json",
                ],
                capture_output=True,
                text=True,
            )

            self.assertNotEqual(0, completed.returncode)
            self.assertIn("unexpected fields: typo", completed.stderr)

    def test_cli_emits_json(self):
        with tempfile.TemporaryDirectory() as directory:
            baseline_path = Path(directory, "baseline.json")
            candidate_path = Path(directory, "candidate.json")
            baseline_path.write_text(
                json.dumps(
                    {
                        "metric": "latency",
                        "unit": "ms",
                        "direction": "lower",
                        "samples": [100, 120, 140],
                    }
                )
            )
            candidate_path.write_text(
                json.dumps(
                    {
                        "metric": "latency",
                        "unit": "ms",
                        "direction": "lower",
                        "samples": [80, 90, 100],
                    }
                )
            )

            completed = subprocess.run(
                [
                    sys.executable,
                    str(Path(__file__).with_name("compare_samples.py")),
                    str(baseline_path),
                    str(candidate_path),
                    "--format",
                    "json",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            payload = json.loads(completed.stdout)

            self.assertEqual(
                {"baseline", "candidate", "deltas", "metric", "unit", "direction"},
                set(payload),
            )


if __name__ == "__main__":
    unittest.main()
