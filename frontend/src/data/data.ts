import raw from "./data.json"

export interface Result {
  context: string
  answer: string
  start_index: number
  end_index: number
}

export interface Question {
  question: string
  summary_answer?: string
  summary_context?: string
  results: Result[]
}

export interface Task {
  task: string
  questions: Question[]
}

const data: Task[] = raw.data
export default data
