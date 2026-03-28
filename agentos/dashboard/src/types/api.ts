export type RunRow = {
  run_id: string
  status: string | null
  workflow_name: string | null
  started_at: string | null
  step_count: number | null
  project?: string | null
}

export type StepRow = {
  id: string
  agent: string | null
  kind?: string | null
  status: string
  requires_approval: boolean
  detail?: Record<string, unknown> | null
}

export type DebateSession = {
  debate_id: string
  step_id?: unknown
  topic?: unknown
  participants?: unknown
  rounds: Record<string, unknown>[]
  evidence: Record<string, unknown>[]
  resolution: Record<string, unknown> | null
}

export type RunDetailResponse = {
  state: Record<string, unknown>
  events: Record<string, unknown>[]
  steps: StepRow[]
  debates?: DebateSession[]
}
