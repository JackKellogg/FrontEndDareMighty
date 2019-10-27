import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';

const theme = {
    spacing: 8,
  }
  
//   <Box m={-2} /> // margin: -16px;
//   <Box m={0} /> // margin: 0px;
//   <Box m={0.5} /> // margin: 4px;
//   <Box m={2} /> // margin: 16px;

const useStyles = makeStyles(theme => ({
  button: {
    margin: theme.spacing(5),
  },
  input: {
    display: 'none',
  },
}));

export default function ContainedButtons() {
  const classes = useStyles();

  return (
    <div>
      
      <Button variant="contained" color="primary" className={classes.button}>
        Enter
      </Button>
      
      {/* <input
        accept="image/*"
        className={classes.input}
        id="contained-button-file"
        multiple
        type="file"
      />
      <label htmlFor="contained-button-file">
        <Button variant="contained" component="span" className={classes.button}>
          Upload
        </Button>
      </label> */}
    </div>
  );
}