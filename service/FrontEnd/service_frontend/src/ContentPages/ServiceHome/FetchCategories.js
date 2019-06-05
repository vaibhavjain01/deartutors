/* eslint-env node, es6 */
import React from "react";
import Axios from "axios";
import * as API_CONSTANTS from "../../Common/APIConstants";
import { Grid, Segment, GridRow, Header } from "semantic-ui-react";

class FetchCategories extends React.Component {
  constructor(props) {
    super(props);
    this.state = { categories_info: "None" };
  }

  componentDidMount() {
    const header = {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("JWTAccess")
      }
    };
    Axios.get(API_CONSTANTS.API_CATEGORIES_URL, header)
      .then(
        function(response) {
          const categories_info = response.data.map(c => {
            return {
              id: c.id,
              name: c.name,
              short_desc: c.short_desc,
              long_desc: c.long_desc
            };
          });

          this.setState({
            categories_info: categories_info
          });
        }.bind(this)
      )
      .catch(error => console.log(error));
  }

  render() {
    const { categories_info } = this.state;

    const names = [];
    for (var i = 0; i < categories_info.length; i++) {
      names.push(categories_info[i]["name"]);
    }

    return (
      <div className="Categories">
        <Segment basic>
          <Grid textAlign="center">
            <GridRow>
              <Header as="h1">Services</Header>
            </GridRow>
            {names.map(function(name, i) {
              return (
                <GridRow key={i}>
                  <Header as="h4">{name}</Header>
                </GridRow>
              );
            })}
          </Grid>
        </Segment>
      </div>
    );
  }
}

export default FetchCategories;
