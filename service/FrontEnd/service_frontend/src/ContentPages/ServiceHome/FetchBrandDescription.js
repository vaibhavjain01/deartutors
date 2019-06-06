/* eslint-env node, es6 */
import React from "react";
import Axios from "axios";
import * as API_CONSTANTS from "../../Common/APIConstants";
import { Grid, Segment, GridRow, Header } from "semantic-ui-react";
import { Template } from "../../Common/HelperComponents/Template";

class FetchBrandDescription extends React.Component {
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
              title: c.title,
              short_desc: c.short_desc,
              long_desc: c.long_desc
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
    const { brand_info } = this.state;
    return (
      <div className="BrandDescription">
        <Segment basic>
          <Grid>
            <GridRow>
              <Header as="h1">{brand_info[0]["title"]}</Header>
            </GridRow>
            <GridRow>
              <Header as="h3">{brand_info[0]["short_desc"]}</Header>
            </GridRow>
            <GridRow>
              <Header as="h5">
                {brand_info ? (
                  <Template>{brand_info[0]["long_desc"]}</Template>
                ) : (
                  "Loading"
                )}
              </Header>
            </GridRow>
          </Grid>
        </Segment>
      </div>
    );
  }
}

export default FetchBrandDescription;
