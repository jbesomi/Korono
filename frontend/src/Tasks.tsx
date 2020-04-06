import React, { useState } from "react"
import Select from "@material-ui/core/Select"
import MenuItem from "@material-ui/core/MenuItem"
import Typography from "@material-ui/core/Typography"

import data from "./data/data"
import TaskView from "./TaskView"

const Tasks: React.FC<{}> = () => {
  const [taskIndex, setTaskIndex] = useState<number | undefined>()

  return (
    <>
      <Typography variant="h6">Select a task</Typography>
      <Select
        value={taskIndex}
        onChange={e => setTaskIndex(e.target.value as number)}
      >
        {data.map((task, index) => (
          <MenuItem value={index}>{task.task}</MenuItem>
        ))}
      </Select>

      {taskIndex !== undefined && <TaskView task={data[taskIndex]} />}
    </>
  )
}

export default Tasks
