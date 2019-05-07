/* eslint-env node, es6 */
import React from "react";
import { Grid, Segment, GridRow, Header } from "semantic-ui-react";

class ServiceHome extends React.Component {
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
