# INC-0001: Mission terminal policy overwritten by user configuration

## Impact
A Project Autopilot executor could not run terminal verification because CLI startup replaced
the dispatcher-injected Docker worktree mount flag with the user's `false` profile value.

## Root cause
Terminal configuration bridging treated file configuration as authoritative even for a mission
worker carrying an explicit fail-closed `HERMES_MISSION_POLICY` and injected `TERMINAL_*` values.

## Repair
Preserve existing dispatcher-injected terminal environment values for mission workers. Added a
regression test covering Docker backend, worktree mount, network-off, and nonpersistent settings.

## Evidence
Hermes commit `c82a8aa10`; 91 focused mission and containment tests passed.
