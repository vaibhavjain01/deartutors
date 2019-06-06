/* eslint-env node, es6 */
import React from "react";
import {
  Grid,
  Segment,
  GridRow,
  Header,
  GridColumn,
  Image
} from "semantic-ui-react";
import { Template } from "../../Common/HelperComponents/Template";

class ServiceCategoryItem extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
    this.state.serviceItem = props.serviceItem;
  }

  render() {
    const { serviceItem } = this.state;
    return (
      <Segment basic color="teal">
        <div className="CategoryServices">
          <Grid>
            <GridColumn width="4">
              <Image size="huge" src={serviceItem["main_pic_url"]} />
            </GridColumn>
            <GridColumn width="12">
              <GridRow>
                <Header as="h3">{serviceItem["name"]}</Header>
              </GridRow>
              <GridRow>
                <br />
              </GridRow>
              <GridRow>
                <Header as="h5">
                  <Template>{serviceItem["short_desc"]}</Template>
                </Header>
              </GridRow>
              <GridRow>
                <br />
              </GridRow>
              <GridRow>
                <Header as="h5">${serviceItem["price"]} per session</Header>
              </GridRow>
              <GridRow>
                <Header as="h5">
                  Minimum session duration: {serviceItem["duration_in_hours"]}{" "}
                  hours and {serviceItem["duration_in_mins"]} minutes
                </Header>
              </GridRow>
            </GridColumn>
          </Grid>
        </div>
      </Segment>
    );
  }
}

export default ServiceCategoryItem;
