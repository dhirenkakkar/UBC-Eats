import React, { Component} from 'react';
import {AppBar,Toolbar,Typography} from '@material-ui/core/'








class Header extends Component {
  render() {
    return (

        <AppBar position="static">
          <Toolbar>
           <Typography variant="headline" color="inherit">
             Cards R Us

           </Typography>
           

         </Toolbar>
        </AppBar>


    );
  }
}

export default Header;
