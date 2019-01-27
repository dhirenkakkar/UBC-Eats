import React, { Component} from 'react';

import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';


class CenterText extends Component {


  render() {
    return (
     <div style={{
        position: 'absolute', left: '50%', top: '50%',
        transform: 'translate(-50%, -50%)'
    }}>
      <Typography variant="h2" color="inherit" align="center" >
                Visualize your spending on campus!
      </Typography>

      <div
    style={{
        position: 'absolute', left: '50%', top: '200%',
        transform: 'translate(-50%, -50%)'
    }}>

      <Button
        type="submit"
        fullWidth
        variant="contained"
        color="primary">
        Sign in with CWL
      </Button>
  
    </div>

    </div>





    );
  }
}

export default CenterText;
