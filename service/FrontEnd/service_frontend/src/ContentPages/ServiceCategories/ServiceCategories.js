/* eslint-env node, es6 */
import React from "react";
import Axios from "axios";
import * as API_CONSTANTS from "../../Common/APIConstants";
import { Grid, Segment, GridRow, Header } from "semantic-ui-react";
import ServiceCategoryItem from "./ServiceCategoryItem";

class ServiceCategories extends React.Component {
  constructor(props) {
    super(props);
    this.state = { categories_info: "", services_info: "" };
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

          Axios.get(API_CONSTANTS.API_SERVICES, header)
            .then(
              function(response) {
                const services_info = response.data.map(c => {
                  return {
                    id: c.id,
                    name: c.name,
                    short_desc: c.short_desc,
                    price: c.price,
                    duration_in_mins: c.duration_in_mins,
                    duration_in_hours: c.duration_in_hours,
                    main_pic_url: c.main_pic_url,
                    category: c.category
                  };
                });
                this.setState({
                  services_info: services_info
                });
              }.bind(this)
            )
            .catch(error => console.log(error));

          this.setState({
            categories_info: categories_info
          });
        }.bind(this)
      )
      .catch(error => console.log(error));
  }

  render() {
    const { categories_info, services_info } = this.state;
    const categories = [];
    const services = [];

    for (var i = 0; i < categories_info.length; i++) {
      categories.push(categories_info[i]);
    }
    for (i = 0; i < services_info.length; i++) {
      services.push(services_info[i]);
    }

    return (
      <div className="Categories">
        <Segment basic>
          <Grid textAlign="center">
            <GridRow>
              <Header as="h1">Service Categories</Header>
            </GridRow>
            <Segment.Group>
              {categories.map(function(category, i) {
                return (
                  <Segment basic padded key={i}>
                    <Segment basic>
                      <Grid>
                        <GridRow>
                          <Header as="h2" color="brown">
                            {category.name}
                          </Header>
                        </GridRow>
                        <GridRow>
                          <Header as="h3">{category.short_desc}</Header>
                        </GridRow>
                        <GridRow>
                          <Header as="h5">
                            <div
                              dangerouslySetInnerHTML={{
                                __html: category.long_desc
                              }}
                            />
                          </Header>
                        </GridRow>
                        <GridRow>
                          <Segment>
                            {services.map(function(service, i) {
                              if (category.name === service.category) {
                                return (
                                  <Header key={i} as="h5">
                                    Matched
                                  </Header>
                                );
                              }
                            })}
                          </Segment>
                        </GridRow>
                      </Grid>
                    </Segment>
                  </Segment>
                );
              })}
            </Segment.Group>
          </Grid>
        </Segment>
      </div>
    );
  }
}

export default ServiceCategories;
