import React, {Component} from 'react';
import Config from '../config/index';

const INITIAL_STATE = {
    jsonData:""
}

class Form extends Component {
    constructor(props) {
        super(props);

        this.state = INITIAL_STATE;
    }

    componentWillMount() {
        fetch(Config.backendAPI).then((data)=>{
            this.setState({jsonData:data})
        })
    }

    render() {
        let data = this.state.jsonData;
        return(
            <div>
                <p>Returned Data:</p>
                {data}
            </div>
        )
    }
}


export default Form;