/* eslint-env node, es6 */
import React from "react";
import Axios from "axios";
import * as API_CONSTANTS from "../../Common/APIConstants";
import { Grid, Segment, GridRow, Header } from "semantic-ui-react";

class ServiceCategoryItem extends React.Component {
  constructor(props) {
    super(props);
    this.state = { service_item_info: undefined };
    this.state.category_name = props.category_name;
    console.log("Calling for " + props.category_name);
  }

  componentDidMount() {
    const header = {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("JWTAccess")
      }
    };
    if (this.state.category_name == undefined) {
      return;
    }
    Axios.get(API_CONSTANTS.API_SERVICES + this.state.category_name, header)
      .then(
        function(response) {
          const service_item_info = response.data.map(c => {
            return {
              fields: c.fields
            };
          });
          this.setState({
            service_item_info: service_item_info
          });
        }.bind(this)
      )
      .catch(error => console.log(error));
  }

  render() {
    const { service_item_info } = this.state;
    return (
      <div className="CategoryServices">
        {service_item_info
          ? service_item_info.map(function(service_item, i) {
              return (
                <Header key={i} as="h5">
                  {service_item["fields"]["name"]}
                </Header>
              );
            })
          : "Loading"}
      </div>
    );
  }
}

export default ServiceCategoryItem;
