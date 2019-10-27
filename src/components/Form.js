import React, {Component} from 'react';
import Config from '../config/index';
import Response from './Response';
// import Snack from './snack';
import FormSelection from './FormSelection';
import button from './button';

const INITIAL_STATE = {
    response: false,
    jsonData:{}
}

class Form extends Component {
    constructor(props) {
        super(props);

        this.state = INITIAL_STATE;
    }

    componentWillMount() {
        fetch(Config.backendAPI + 'yo').then(data=>data.json())
        .then(jsonData => {
            this.setState({jsonData:jsonData,response:true})
        })
        .catch(e => {
            this.setState({error: true});
            console.log("Error! ", e);
        })
    }

    
      

    render() {
        let info = {
            "Address":"1234 Dumb St.",
            "Name":"Jack's Building",
            "Cost":"1,001,999,999,999,009"
        }

        let data = this.state.jsonData;
        var z = JSON.stringify(data)
//        var re = new RegExp(, 'g');
        z = z.replace(/\\\"/g, "\"")
        console.log(z)
        return(
            
            <div>
                {/* <Snack /> */}
                {/* <p>Returned Data:</p>
                {JSON.stringify(data)} */}
                {this.state.response ? <Response info={data}/>:<p>No Data</p>}

                <FormSelection/>
                <button/>
                
                {JSON.stringify(z)}//JSON.stringify(data)}
            </div>

        )
    }
}


export default Form;