import React from "react"
import AppBar from "@material-ui/core/AppBar"
import Toolbar from "@material-ui/core/Toolbar"
import Typography from "@material-ui/core/Typography"
import makeStyles from "@material-ui/core/styles/makeStyles"

const useStyles = makeStyles({
  logo: {
    marginRight: 20
  }
})

const App: React.FC<{}> = () => {
  const classes = useStyles()
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h3" className={classes.logo}>
          👑
        </Typography>
        <Typography variant="h5">Korono</Typography>
      </Toolbar>
    </AppBar>
  )
}
export default App
