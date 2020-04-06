import React from "react"
import Typography from "@material-ui/core/Typography"
import makeStyles from "@material-ui/core/styles/makeStyles"

import { Question } from "./data/data"

const useStyles = makeStyles({
  title: {
    marginTop: 40
  }
})

const QuestionView: React.FC<{ question: Question }> = ({ question }) => {
  const classes = useStyles()

  return (
    <>
      <Typography variant="h5" className={classes.title}>
        {`${question.question}?`}
      </Typography>

      {question.results.map(result => (
        <p>{result.context}</p>
      ))}
    </>
  )
}

export default QuestionView
