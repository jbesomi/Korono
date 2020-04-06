import React, { useState } from "react"
import Select from "@material-ui/core/Select"
import MenuItem from "@material-ui/core/MenuItem"
import Typography from "@material-ui/core/Typography"
import makeStyles from "@material-ui/core/styles/makeStyles"

import { Task } from "./data/data"
import QuestionView from "./QuestionView"

const useStyles = makeStyles({
  title: {
    marginTop: 40
  }
})

const TaskView: React.FC<{ task: Task }> = ({ task }) => {
  const classes = useStyles()
  const [questionIndex, setQuestionIndex] = useState<number | undefined>()

  return (
    <>
      <Typography variant="h6" className={classes.title}>
        Select a question
      </Typography>
      <Select
        value={questionIndex}
        onChange={e => setQuestionIndex(e.target.value as number)}
      >
        {task.questions.map((question, index) => (
          <MenuItem value={index}>{question.question}</MenuItem>
        ))}
      </Select>

      {questionIndex !== undefined && (
        <QuestionView question={task.questions[questionIndex]} />
      )}
    </>
  )
}

export default TaskView
