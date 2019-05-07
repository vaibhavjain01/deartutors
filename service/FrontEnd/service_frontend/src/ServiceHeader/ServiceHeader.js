/* eslint-env node, es6 */
import React from "react";
import { Grid, Segment, GridColumn } from "semantic-ui-react";
import ServiceMenu from "./ServiceMenu/ServiceMenu";

class ServiceHeader extends React.Component {
  render() {
    const { header_bg_color } = this.props;

    return (
      <div className="ServiceHeader">
        <Segment padded color={header_bg_color} inverted>
          <Grid>
            <Grid.Row>
              <Grid.Column width="9"> Logo</Grid.Column>
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
