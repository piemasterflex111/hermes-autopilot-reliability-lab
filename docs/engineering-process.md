# Engineering Process

## Work intake

Every change starts as an issue containing: problem, observable outcome, non-goals, allowed
paths, dependencies, verification commands, risks, and rollback. Work stays in triage until it
satisfies the Definition of Ready.

## Execution

One implementation mission is active at a time. Work occurs in a branch or isolated worktree.
Changes remain small enough to review as one coherent decision. The engineer records commands,
test results, and important decisions while working rather than reconstructing them afterward.

## Review and release

Pull requests include a scope summary, evidence, residual risks, rollback, and documentation
changes. CI must pass before merge. Architectural decisions require an ADR. Every defect gets a
reproducer and regression test. Each completed milestone receives a semantic version tag and a
concise release note.

## Incident response

Stop mutation, preserve evidence, reproduce the failure, identify the violated invariant, write
a regression test, implement the narrowest repair, verify broadly, and record the incident.
