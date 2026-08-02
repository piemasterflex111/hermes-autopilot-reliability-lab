# Threat Model

## Protected assets
Source repositories, Git history, verification evidence, credentials, benchmark integrity, and
operator approval authority.

## Initial threats
- executor changes tests or verification commands to manufacture success;
- stale evidence from an older run is accepted;
- contradictory checkpoints both appear current;
- path confusion mutates a nested or unintended repository;
- model prose is treated as authoritative evidence;
- network or credentials escape the declared mission boundary.

## Milestone 0 controls
Strict process gates, typed identities, CI, coverage, documentation, incident records, and
explicit non-goals. Runtime containment and authorization controls belong to later milestones.
