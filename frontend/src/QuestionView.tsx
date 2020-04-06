import React from "react"
import Typography from "@material-ui/core/Typography"
import Card from "@material-ui/core/Card"
import CardContent from "@material-ui/core/CardContent"
import makeStyles from "@material-ui/core/styles/makeStyles"

import { Question } from "./data/data"

const useStyles = makeStyles({
  title: {
    marginTop: 40
  },
  card: {
    marginTop: 20,
    marginBottom: 20
  }
})

const QuestionView: React.FC<{ question: Question }> = ({ question }) => {
  const classes = useStyles()

  return (
    <>
      <Typography variant="h5" className={classes.title}>
        {`${question.question}?`}
      </Typography>

      {question.results.map(result => {
        const before = result.context.slice(0, result.start_index)
        const answer = result.context.slice(
          result.start_index,
          result.end_index
        )
        const after = result.context.slice(result.end_index, -1)

        return (
          <Card className={classes.card} variant="outlined">
            <CardContent>
              <Typography display="inline" variant="body1">
                {before}
              </Typography>
              <Typography display="inline" variant="body1" color="primary">
                <b>{answer}</b>
              </Typography>
              <Typography display="inline" variant="body1">
                {after}
              </Typography>
            </CardContent>
          </Card>
        )
      })}
    </>
  )
}

export default QuestionView
