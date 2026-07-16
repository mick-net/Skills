# SaaS Performance Hillclimb Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build, install, and publish a reusable `saas-performance-hillclimb` skill for evidence-backed SQL, API/server, server-rendering, and browser performance experiments.

**Architecture:** Keep the universal experiment contract and safety boundaries in a concise `SKILL.md`. Route layer-specific work to four one-level references, and provide one standard-library Python comparator for projects without native baseline/candidate comparison tooling. Maintain the public skill folder as source and install an identical global copy.

**Tech Stack:** Markdown Agent Skills, YAML agent metadata, Python 3 standard library, `unittest`, Git.

## Global Constraints

- Optimize performance only; treat correctness, reliability, error rate, resource use, and cost as guardrails.
- Optimize one behavior class and one primary metric at a time.
- Separate cold-cache, warm-cache, concurrency, dataset-size, geographic, device, and network scenarios when they represent different user experiences.
- Prefer repeated baseline/candidate measurements and distributions over single runs or averages.
- Require correctness and holdout/sentinel protection before keeping an optimization.
- Treat production load tests, cache flushes, index/schema/config changes, and traffic shifts as state-changing operations requiring explicit authority and a rollback path.
- Reuse project-native performance tooling before introducing the fallback comparator.
- Keep `/Users/mickvermaat/Github/Skills/saas-performance-hillclimb` and `/Users/mickvermaat/.codex/skills/saas-performance-hillclimb` identical before publication.
- Leave unrelated `microsoft-clarity/` and `saas-revenue-cro/` working-tree content untouched.

---

### Task 1: Scaffold and Author the Skill Workflow

**Files:**
- Create: `saas-performance-hillclimb/SKILL.md`
- Create: `saas-performance-hillclimb/agents/openai.yaml`
- Create: `saas-performance-hillclimb/references/experiment-loop.md`
- Create: `saas-performance-hillclimb/references/sql-performance.md`
- Create: `saas-performance-hillclimb/references/api-and-server-performance.md`
- Create: `saas-performance-hillclimb/references/web-client-performance.md`
- Create: `saas-performance-hillclimb/references/experiment-record.md`

**Interfaces:**
- Consumes: `docs/superpowers/specs/2026-07-16-saas-performance-hillclimb-design.md`.
- Produces: a skill whose `SKILL.md` directly links every reference and whose frontmatter name is exactly `saas-performance-hillclimb`.

- [ ] **Step 1: Initialize the required skill shape**

Run:

```bash
python3 /Users/mickvermaat/.codex/skills/.system/skill-creator/scripts/init_skill.py saas-performance-hillclimb \
  --path /Users/mickvermaat/Github/skills/.worktrees/saas-performance-hillclimb \
  --resources scripts,references \
  --interface 'display_name=SaaS Performance Hillclimb' \
  --interface 'short_description=Run evidence-backed SaaS speed experiments' \
  --interface 'default_prompt=Use $saas-performance-hillclimb to benchmark this slow SaaS path, localize the bottleneck, and run one safe baseline-versus-candidate experiment.'
```

Expected: a new `saas-performance-hillclimb/` directory containing `SKILL.md`, `agents/openai.yaml`, `scripts/`, and `references/`.

- [ ] **Step 2: Replace the generated instructions with the approved workflow**

Write `SKILL.md` with only `name` and `description` in frontmatter. Make the description trigger on slow SQL queries, APIs, backend/server work, SSR/TTFB, page loads, Core Web Vitals, Lighthouse, LCP, INP, CLS, profiling, load tests, and performance regressions. Include:

```markdown
## First Checks

1. Identify the owning repository, production boundary, user-visible scenario, and existing performance tooling.
2. Read performance specs, experiment history, telemetry, and `git status --short` before interpreting measurements.
3. Reproduce the slow path without changing production state.
4. Define one primary metric, guardrails, environment fingerprint, cache state, data shape, concurrency, repetitions, and stop conditions.
5. Choose an optimization pack plus at least one holdout, sentinel, or adjacent workload.
```

Add the approved bottleneck classes, universal loop, keep/revert rules, safety boundaries, durable experiment-record fallback, and conditional links to every reference.

- [ ] **Step 3: Write the layer playbooks and experiment template**

Populate the references with direct operational guidance:

- `experiment-loop.md`: measurement contract, baseline, localization, one-variable hypothesis, repeated candidate, sentinel validation, keep/revert log.
- `sql-performance.md`: query-plan-first diagnosis, representative cardinality, cache/buffer distinction, index write costs, lock/contention/pool checks, and safe `EXPLAIN ANALYZE` warnings.
- `api-and-server-performance.md`: request timing decomposition, traces/profiles, dependency time, serialization, concurrency/load shapes, load-generator saturation, Server Timing, and SSR/TTFB waterfalls.
- `web-client-performance.md`: lab-versus-field separation, repeated Lighthouse runs, LCP/INP/CLS diagnostics, resource waterfalls, main-thread work, device/network profiles, and SEO performance scope.
- `experiment-record.md`: a copyable record with scenario, metric, guardrails, environment, baseline, trace evidence, hypothesis, candidate, holdout, decision, rollback, and next experiment.

Include the primary-source URLs from the design spec near the guidance they support.

- [ ] **Step 4: Validate the skill metadata and links**

Run:

```bash
python3 /Users/mickvermaat/.codex/skills/.system/skill-creator/scripts/quick_validate.py saas-performance-hillclimb
rg -n 'references/(experiment-loop|sql-performance|api-and-server-performance|web-client-performance|experiment-record)\.md' saas-performance-hillclimb/SKILL.md
```

Expected: `Skill is valid!` and at least one direct `SKILL.md` link for each reference.

- [ ] **Step 5: Commit the workflow slice**

```bash
git add saas-performance-hillclimb/SKILL.md saas-performance-hillclimb/agents saas-performance-hillclimb/references
git commit -m "feat: add SaaS performance hillclimb workflow"
```

### Task 2: Add a Tested Baseline/Candidate Comparator

**Files:**
- Create: `saas-performance-hillclimb/scripts/test_compare_samples.py`
- Create: `saas-performance-hillclimb/scripts/compare_samples.py`
- Modify: `saas-performance-hillclimb/SKILL.md`

**Interfaces:**
- Consumes: baseline and candidate JSON objects shaped as `{"metric": str, "unit": str, "direction": "lower"|"higher", "samples": list[number]}`.
- Produces: `load_sample_set(path) -> SampleSet`, `summarize(samples) -> dict[str, float|int]`, `compare(baseline, candidate) -> dict`, and CLI `compare_samples.py BASELINE CANDIDATE [--format text|json]`.

- [ ] **Step 1: Write failing unit tests**

Create `test_compare_samples.py` with `unittest` cases that import `compare_samples` and assert:

```python
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

def test_cli_emits_json(self):
    with tempfile.TemporaryDirectory() as directory:
        baseline_path = Path(directory, "baseline.json")
        candidate_path = Path(directory, "candidate.json")
        baseline_path.write_text(json.dumps({
            "metric": "latency", "unit": "ms", "direction": "lower",
            "samples": [100, 120, 140]
        }))
        candidate_path.write_text(json.dumps({
            "metric": "latency", "unit": "ms", "direction": "lower",
            "samples": [80, 90, 100]
        }))
        completed = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("compare_samples.py")),
             str(baseline_path), str(candidate_path), "--format", "json"],
            check=True, capture_output=True, text=True,
        )
        payload = json.loads(completed.stdout)
        self.assertEqual({"baseline", "candidate", "deltas", "metric", "unit", "direction"}, set(payload))
```

Import `json`, `subprocess`, `sys`, `tempfile`, and `Path` for the CLI test.

- [ ] **Step 2: Run tests and confirm RED**

Run:

```bash
python3 -m unittest saas-performance-hillclimb/scripts/test_compare_samples.py -v
```

Expected: FAIL because `compare_samples` does not exist.

- [ ] **Step 3: Implement the minimal comparator**

Use only Python's standard library. Implement immutable `SampleSet`, linear-interpolated percentiles, count/min/max/mean/median/p90/p95/p99, metadata validation, absolute and percentage deltas, direction-aware `improvement_percent`, JSON output, and concise text output. Reject booleans, non-numeric/non-finite values, and sample lists shorter than two. Represent percentage delta as `null` when the baseline statistic is zero.

- [ ] **Step 4: Run tests and CLI smoke checks**

Run:

```bash
python3 -m unittest saas-performance-hillclimb/scripts/test_compare_samples.py -v
```

Expected: all unit tests pass, including the subprocess CLI smoke test that validates JSON containing `baseline`, `candidate`, and `deltas`.

- [ ] **Step 5: Link the fallback tool and commit**

Add a short `SKILL.md` fallback-tool section that says to prefer project-native comparison tooling and documents the input shape and command. Then run `quick_validate.py` and commit:

```bash
git add saas-performance-hillclimb/SKILL.md saas-performance-hillclimb/scripts
git commit -m "feat: compare SaaS performance samples"
```

### Task 3: Index, Install, Validate, and Publish

**Files:**
- Modify: `README.md`
- Copy: `saas-performance-hillclimb/` to `/Users/mickvermaat/.codex/skills/saas-performance-hillclimb/`

**Interfaces:**
- Consumes: validated public source skill from Tasks 1-2.
- Produces: discoverable README entry, identical global installation, scoped Git commits, and published `master` history.

- [ ] **Step 1: Add the public skill index entry**

Add this bullet under `## Skills`:

```markdown
- `saas-performance-hillclimb`: improve SQL, API, server-rendering, and browser speed through controlled baseline-versus-candidate experiments.
```

- [ ] **Step 2: Validate source, tests, and metadata**

Run:

```bash
python3 /Users/mickvermaat/.codex/skills/.system/skill-creator/scripts/quick_validate.py saas-performance-hillclimb
python3 -m unittest saas-performance-hillclimb/scripts/test_compare_samples.py -v
python3 -m py_compile saas-performance-hillclimb/scripts/compare_samples.py saas-performance-hillclimb/scripts/test_compare_samples.py
```

Expected: validation succeeds, all tests pass, and compilation exits zero.

- [ ] **Step 3: Install the complete skill globally**

Remove only a pre-existing `saas-performance-hillclimb` destination if it was created by this task, then copy the complete source folder to `/Users/mickvermaat/.codex/skills/saas-performance-hillclimb`. Do not alter any other global skill.

- [ ] **Step 4: Verify installed copy and parity**

Run:

```bash
python3 /Users/mickvermaat/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/mickvermaat/.codex/skills/saas-performance-hillclimb
diff -rq saas-performance-hillclimb /Users/mickvermaat/.codex/skills/saas-performance-hillclimb
```

Expected: installed skill is valid and `diff` emits no output.

- [ ] **Step 5: Forward-test three independent scenarios**

Dispatch fresh validators with only the skill path and one synthetic task each: SQL-backed API latency, SSR/high TTFB, and poor LCP/INP. Require each output to define a baseline before edits, distinguish relevant cache/load states, use percentile or Core Web Vital distributions, retain correctness/error sentinels, and avoid production-impacting operations without authority.

- [ ] **Step 6: Commit the index and any validated refinements**

```bash
git add README.md saas-performance-hillclimb docs/superpowers/plans/2026-07-16-saas-performance-hillclimb.md
git commit -m "docs: publish SaaS performance hillclimb skill"
```

- [ ] **Step 7: Integrate and publish**

After whole-branch review, fast-forward local `master` to `codex/saas-performance-hillclimb`, verify the original checkout still contains only the pre-existing unrelated untracked folders, and push `master` to `origin`.

Expected: `origin/master` contains the new skill, README entry, design, plan, comparator tests, and scoped worktree-ignore change.
