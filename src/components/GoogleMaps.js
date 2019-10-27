import React from 'react';
// import { URL, URLSearchParams } from 'url';
import querystring from 'querystring';
// import axios from 'axios';

export default function ControlledExpansionPanels(props) {

    var url = 'https://maps.googleapis.com/maps/api/streetview';

    var params = {
        size: '400x400',
        location: props.params.lat+','+props.params.long,
        fov:80,
        heading:70,
        pitch:0,
        key:'AIzaSyB0OUUevHIAzgoXO_W_8EPOxMbPagtceZU'
    } // or:
    // var params = [['lat', '35.696233'], ['long', '139.570431']]

    url = url +'?'+ querystring.stringify(params);
    // let string = new URLSearchParams(params);

    console.log(url);
  return (
    <div>
        <img src={url} alt="Street View Image" />        
      
    </div>
  );
}