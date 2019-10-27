import React, {Component} from 'react';

import Dropdown from './dropdown';
import Table from './Table';
import StreetMaps from './GoogleMaps';

const params = {
    size: '400x400',
    lat: 47.5763831,
    long:-122.4211769,
    fov:80,
    heading:70,
    pitch:0,
    key:'AIzaSyB0OUUevHIAzgoXO_W_8EPOxMbPagtceZU'
}

class Form extends Component {
    constructor(props) {
        super(props);
        console.log(this.props.info)
        this.state = {
            info: this.props.info
        }
    }

    

    render() {
        var formatted = [];
        var data = this.state.info;

        if(data) {
            for(var key in data) {
                formatted.push(<p>{key} : {data[key]}</p>);
            }
        }

        return(
            <div>
                {/* <Dropdown info={this.state.info} /> */}

                <Table info={this.state.info} />
                <StreetMaps params={params} />
                {/* {formatted} */}
            </div>
        )
    }
}


export default Form;