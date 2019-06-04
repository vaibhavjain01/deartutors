/* eslint-env node, es6 */
import React from "react";
import { Grid, Segment } from "semantic-ui-react";
import Axios from "axios";
import * as API_CONSTANTS from "../Common/APIConstants";
import { Image } from "semantic-ui-react";

class ServiceHeader extends React.Component {
  constructor(props) {
    super(props);
    this.state = { brand_info: "None" };
  }

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

  render_logo_image() {
    const { brand_info } = this.state;
    return <Image src={brand_info[0]["logo_image_url"]} />;
  }

  render() {
    const { header_bg_color } = this.props;
    const { brand_info } = this.state;

    return (
      <div className="ServiceHeader">
        <Segment padded color={header_bg_color}>
          <Grid>
            <Grid.Row>
              <Grid.Column width="9">{this.render_logo_image()}</Grid.Column>
              <Grid.Column width="3">
                {brand_info[0]["contact_number"]}
              </Grid.Column>
              <Grid.Column width="4"> {brand_info[0]["email"]}</Grid.Column>
            </Grid.Row>
          </Grid>
        </Segment>
      </div>
    );
  }
}

export default ServiceHeader;
