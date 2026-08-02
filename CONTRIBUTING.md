# Contributing

## Required workflow

1. Open an issue with the problem, observable outcome, non-goals, allowed paths, risks, and verification commands.
2. Confirm the issue satisfies the Definition of Ready.
3. Create a focused branch or isolated worktree; never implement directly on `main`.
4. Make the smallest coherent change and add deterministic tests.
5. Run `make verify` locally.
6. Open a pull request with evidence, risks, rollback, and the final diff scope.
7. Resolve review comments and merge only after required checks pass.

Architectural changes require an ADR. Defect fixes require a reproducer and regression test.
Do not combine unrelated refactoring, feature work, and formatting in one pull request.
