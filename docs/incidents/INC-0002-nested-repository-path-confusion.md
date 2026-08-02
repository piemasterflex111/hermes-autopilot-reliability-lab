# INC-0002: Executor created nested repositories inside the mission worktree

## Impact
A foundation task interpreted host workspace paths as project targets and created multiple
nested Git repositories instead of editing the existing worktree root.

## Violated invariant
A mission must mutate only the declared repository root and allowed relative paths.

## Current disposition
The mission was paused and rolled back. The partial result was not promoted or published.

## Required prevention
Future runner work must normalize host/container paths, state `/workspace` as the only terminal
root, reject nested repository initialization unless explicitly allowed, and classify unexpected
`.git` directories as unsafe success.
