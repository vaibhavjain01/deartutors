/* eslint-env node, es6 */
import React from "react";
import { Grid, Segment, GridColumn } from "semantic-ui-react";
import ServiceMenu from "./ServiceMenu/ServiceMenu";
import Axios from "axios";
import * as API_CONSTANTS from "../Common/APIConstants";
import { Image } from "semantic-ui-react";

class ServiceHeader extends React.Component {
  constructor(props) {
    super(props);
    this.state = { brand_info: "None" };
  }

  componentDidMount() {
    console.log(API_CONSTANTS.API_BRAND_URL);
    const header = {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("JWTAccess")
      }
    };
    Axios.get(API_CONSTANTS.API_BRAND_URL, header)
      .then(function(response) {
        console.log(response);
        const brand_info = response.data.map(c => {
          return { id: c.id, name: c.name };
        });

        const newState = Object.assign({}, this.state, {
          brand_info: brand_info
        });

        this.setState(newState);
      })
      .catch(error => console.log(error));
  }

  render_logo_image() {
    const { brand_info } = this.state;
    console.log(brand_info);
    return <Image src={brand_info["logo_image_url"]} />;
  }

  render() {
    const { header_bg_color } = this.props;

    return (
      <div className="ServiceHeader">
        <Segment padded color={header_bg_color} inverted>
          <Grid>
            <Grid.Row>
              <Grid.Column width="9">{this.render_logo_image()}</Grid.Column>
              <Grid.Column width="3"> Telephone</Grid.Column>
              <Grid.Column width="4"> Email</Grid.Column>
            </Grid.Row>

            <Grid.Row>
              <GridColumn width="16">
                <ServiceMenu />
              </GridColumn>
            </Grid.Row>
          </Grid>
        </Segment>
      </div>
    );
  }
}

export default ServiceHeader;
