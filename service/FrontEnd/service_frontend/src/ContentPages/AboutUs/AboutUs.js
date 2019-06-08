/* eslint-env node, es6 */
import React from "react";
import * as API_CONSTANTS from "../../Common/APIConstants";
import {
  Segment,
  Image,
  Grid,
  GridRow,
  GridColumn,
  Header,
  Divider,
  Button
} from "semantic-ui-react";
import Axios from "axios";
import { Template } from "../../Common/HelperComponents/Template";
import { Document, Page, pdfjs } from "react-pdf";

pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${
  pdfjs.version
}/pdf.worker.js`;

class AboutUs extends React.Component {
  constructor(props) {
    super(props);
    this.state = { about_info: "" };
  }

  componentDidMount() {
    const header = {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("JWTAccess")
      }
    };
    Axios.get(API_CONSTANTS.API_ABOUTUS_URL, header)
      .then(
        function(response) {
          const about_info = response.data.map(c => {
            return {
              id: c.id,
              title: c.title,
              image: c.image,
              short_description: c.short_description,
              long_description: c.long_description,
              resume_pdf: c.resume_pdf
            };
          });

          this.setState({
            about_info: about_info
          });
          console.log(about_info);
        }.bind(this)
      )
      .catch(error => console.log(error));
  }

  render() {
    const { about_info } = this.state;

    const download_resume = () => {
      var win = window.open(about_info[0]["resume_pdf"], "_blank");
      win.focus();
    };

    return (
      <div className="ContactUs">
        <Segment basic>
          <Grid columns={2} stackable>
            <Divider vertical />
            <GridRow verticalAlign="middle">
              <GridColumn width="8">
                <GridRow>
                  <Header as="h1" textAlign="center">
                    {about_info ? about_info[0]["title"] : "Loading"}
                  </Header>
                  <br />
                  <br />
                </GridRow>
                <GridRow>
                  <Header as="h3" textAlign="center">
                    {about_info
                      ? about_info[0]["short_description"]
                      : "Loading"}
                  </Header>
                  <br />
                  <br />
                </GridRow>
                <GridRow>
                  <Template>
                    {about_info ? about_info[0]["long_description"] : "Loading"}
                  </Template>
                </GridRow>
              </GridColumn>
              <GridColumn width="8">
                <GridRow>
                  {about_info ? (
                    <Image size="huge" src={about_info[0]["image"]} />
                  ) : (
                    "Loading"
                  )}
                </GridRow>
              </GridColumn>
            </GridRow>
          </Grid>
        </Segment>
        <Segment basic color="teal">
          <Grid stackable textAlign="center">
            <GridColumn>
              <Button onClick={download_resume}>Download Resume</Button>
            </GridColumn>
          </Grid>

          <Grid columns={2} stackable textAlign="center">
            <GridRow>
              <Segment>
                <GridColumn width="16">
                  {about_info ? (
                    <Document
                      file={about_info[0]["resume_pdf"]}
                      textAlign="center"
                    >
                      <Page pageIndex={0} />
                    </Document>
                  ) : (
                    "Loading"
                  )}
                </GridColumn>
              </Segment>
            </GridRow>
          </Grid>
        </Segment>
      </div>
    );
  }
}

export default AboutUs;
