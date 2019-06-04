/* eslint-env node, es6 */
import React from "react";
import Axios from "axios";
import * as API_CONSTANTS from "../../Common/APIConstants";
import { Grid, Segment, GridRow, Header } from "semantic-ui-react";

class ServiceHome extends React.Component {
  componentDidMount() {
    const header = {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("JWTAccess")
      }
    };
    Axios.get(API_CONSTANTS.API_BRAND_URL, header)
      .then(
        function(response) {
          const brand_info = response.data.map(c => {
            return {
              id: c.id,
              name: c.name,
              logo_image_url: c.logo_image_url,
              contact_number: c.contact_number,
              email: c.email
            };
          });

          this.setState({
            brand_info: brand_info
          });
        }.bind(this)
      )
      .catch(error => console.log(error));
  }

  render() {
    return (
      <div className="ServiceHome">
        <Segment basic>
          <Grid>
            <GridRow>
              <Header as="h1">Brand Header</Header>
            </GridRow>
            <GridRow>
              <Header as="h3">Brand Short Description</Header>
            </GridRow>
            <GridRow>
              <Header as="h5">Brand Long Description</Header>
            </GridRow>
          </Grid>
        </Segment>
      </div>
    );
  }
}

export default ServiceHome;
