/* eslint-env node, es6 */
import React from "react";
import * as API_CONSTANTS from "../../Common/APIConstants";
import { Segment, Input, Form, TextArea, Button } from "semantic-ui-react";
import { FilePond } from "react-filepond";
import "filepond/dist/filepond.min.css";

class ContactUs extends React.Component {
  constructor(props) {
    super(props);
    this.state = { temp_uploads: [], email: "", phone: "", message: "" };
  }

  render() {
    const handleProcessFile = (error, file) => {
      console.log(file);
      console.log(file.serverId);
      this.setState({
        temp_uploads: this.state.temp_uploads.concat([file.serverId])
      });
    };

    const onChangeEmail = event => {
      this.setState({ email: event.target.value });
    };
    const onChangePhone = event => {
      this.setState({ phone: event.target.value });
    };
    const onChangeMessage = event => {
      this.setState({ message: event.target.value });
    };
    const handleSubmit = event => {
      const message = this.state.message;
      const email = this.state.email;
      const phone = this.state.phone;
      console.log(message + email + phone);
    };

    return (
      <div className="ContactUs">
        <Segment>
          <Form>
            <Form.Group widths="equal">
              <Form.Field
                id="form-input-control-name"
                control={Input}
                label="Email"
                placeholder="Email"
                onChange={onChangeEmail}
                value={this.state.email}
              />
              <Form.Field
                id="form-input-control-last-name"
                control={Input}
                label="Phone"
                placeholder="Phone"
                onChange={onChangePhone}
                value={this.state.phone}
              />
            </Form.Group>
            <Form.Field>
              <FilePond
                server={API_CONSTANTS.API_FILE_UPLOAD}
                onprocessfile={handleProcessFile}
              />
            </Form.Field>
            <Form.Field
              id="form-textarea-control-opinion"
              control={TextArea}
              label="Message"
              placeholder="Message"
              onChange={onChangeMessage}
              value={this.state.message}
            />
            <Form.Field
              id="form-button-control-public"
              control={Button}
              content="Submit"
              label="I will get back to you as soon as possible"
              onClick={handleSubmit}
            />
          </Form>
        </Segment>
      </div>
    );
  }
}

export default ContactUs;
