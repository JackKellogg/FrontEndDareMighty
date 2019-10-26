import React, {Component} from 'react';

const INITIAL_STATE = {
    jsonData:""
}

class Form extends Component {
    constructor(props) {
        super(props);

        this.state = INITIAL_STATE;
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