import React from "react"
import AppBar from "@material-ui/core/AppBar"
import Toolbar from "@material-ui/core/Toolbar"
import Typography from "@material-ui/core/Typography"
import Container from "@material-ui/core/Container"
import Paper from "@material-ui/core/Paper"
import makeStyles from "@material-ui/core/styles/makeStyles"

import Tasks from "./Tasks"

const useStyles = makeStyles(theme => ({
  logo: {
    marginRight: 20
  },

  appBarSpacer: theme.mixins.toolbar,
  content: {
    flexGrow: 1,
    height: "100vh",
    overflow: "auto"
  },
  container: {
    paddingTop: theme.spacing(4),
    paddingBottom: theme.spacing(4)
  },
  paper: {
    padding: theme.spacing(2),
    display: "flex",
    overflow: "auto",
    flexDirection: "column"
  }
}))

const App: React.FC<{}> = () => {
  const classes = useStyles()
  return (
    <>
      <AppBar>
        <Toolbar>
          <Typography variant="h3" className={classes.logo}>
            <span role="img" aria-label="img">
              👑
            </span>
          </Typography>
          <Typography variant="h5">Korono</Typography>
        </Toolbar>
      </AppBar>
      <main className={classes.content}>
        <div className={classes.appBarSpacer} />
        <Container className={classes.container}>
          <Paper className={classes.paper}>
            <Tasks />
          </Paper>
        </Container>
      </main>
    </>
  )
}
export default App
