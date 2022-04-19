import React from "react";


class BookForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {'name': '', 'author': 0}
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )
    }

    handleSubmit(event) {

        this.props.createBook(this.state.name,this.state.author)
        event.preventDefault()
    }


    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="name">name</label>
                    <input type="text" name="name" placeholder="name" value={this.state.name}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label for="author">author</label>
                    <input type="number" name="author" placeholder="author" value={this.state.author}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <input type="submit" value="Save"/>
            </form>
        );
    }


}

export default BookForm