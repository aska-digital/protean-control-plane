# Execution receipt — template (v1.0.0)

    cluster: <recommendation id / cluster name>
    decision record: <path> (status at handoff: <OPEN/RESOLVED>)
    execution lane dir: <path>
    facilitator: <role>

## Per-recommendation status

| rec | executed by | receipt path | terminal marker | read back |
|---|---|---|---|---|
| A1 | <seat / lane> | <path> | COMPLETE / BLOCKED <reason> | <UTC + verifier> |

## Read-backs (integrator verification, not self-report)

- <artifact>: read back on disk, terminal marker <...>, verified by <command>
- <tool result>: re-run by the integrator, exit <n>

## Operator decisions still held

- <gate>: still held by the operator; no canonical edit made.

Terminal line: COUNCIL EXECUTION COMPLETE <path> | BLOCKED <reason>
