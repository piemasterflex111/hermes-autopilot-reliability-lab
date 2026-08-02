# Architecture

## System objective

Determine whether an autonomous repository mission is correct using evidence independent of
the executor's success claim.

## Planned boundaries

| Component | Responsibility | Trust posture |
|---|---|---|
| Contract loader | Parse expected outcome, constraints, and verification | Untrusted input, schema validated |
| Isolated runner | Execute one benchmark in a clean worktree | Mutating, tightly scoped |
| Evidence ledger | Store commands, exit codes, artifacts, hashes, and lineage | Append-oriented system of record |
| Read-only verifier | Compare contract, evidence, and final repository state | Cannot mutate the subject worktree |
| Classifier | Label false completion, partial implementation, stale evidence, contradictory recovery, or unsafe success | Deterministic rules first |
| Reporter | Publish raw and summarized reproducible results | Derived from immutable records |

## Milestone 0 implementation

Only the typed benchmark identity model and repository engineering system are implemented.
No runner, evidence database, model adapter, queue, network service, or classifier exists yet.

## Core invariants

- Executor prose is never sufficient evidence of completion.
- Verification is executed from a clean, identified repository state.
- Evidence belongs to one run lineage and cannot silently satisfy another run.
- A newer checkpoint must explicitly supersede an older checkpoint.
- Passing tests do not imply safety when the contract or tests were modified outside scope.
- Raw artifacts remain available behind every summarized result.
