/* eslint-env node, es6 */
import React from "react";
import { Grid, Segment, GridColumn, GridRow } from "semantic-ui-react";
import FetchBrandDescription from "./FetchBrandDescription";
import FetchCategories from "./FetchCategories";
import FetchHours from "./FetchHours";

class ServiceHome extends React.Component {
  constructor(props) {
    super(props);
    this.state = { brand_info: "None" };
  }

  render() {
    return (
      <div className="ServiceHome">
        <Segment basic>
          <Grid>
            <GridRow>
              <GridColumn width="8">
                <FetchBrandDescription />
              </GridColumn>
            </GridRow>
          </Grid>
        </Segment>
      </div>
    );
  }
}

export default ServiceHome;
