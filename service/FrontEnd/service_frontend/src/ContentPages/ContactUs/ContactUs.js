/* eslint-env node, es6 */
import React from "react";
import * as API_CONSTANTS from "../../Common/APIConstants";
import { Segment, Input, Form, TextArea, Button } from "semantic-ui-react";
import { FilePond } from "react-filepond";
import "filepond/dist/filepond.min.css";
import Axios from "axios";

class ContactUs extends React.Component {
  constructor(props) {
    super(props);
    this.state = { temp_uploads: [], email: "", subject: "", message: "" };
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
    const onChangeSubject = event => {
      this.setState({ subject: event.target.value });
    };
    const onChangeMessage = event => {
      this.setState({ message: event.target.value });
    };
    const handleSubmit = event => {
      const message = this.state.message;
      const email = this.state.email;
      const subject = this.state.subject;
      const file_uploads = this.state.temp_uploads;

      const post_data = {
        email: email,
        subject: subject,
        message: message,
        uploaded_file_ids: file_uploads
      };

      console.log(post_data);

      Axios.post(API_CONSTANTS.API_CONTACT_US_NEW, post_data).catch(error =>
        console.log(error)
      );

      this.setState({ temp_uploads: [], email: "", subject: "", message: "" });
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
                label="Subject"
                placeholder="Subject"
                onChange={onChangeSubject}
                value={this.state.subject}
              />
            </Form.Group>
            <Form.Field>
              <FilePond
                ref={ref => (this.pond = ref)}
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
