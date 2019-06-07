/* eslint-env node, es6 */
import React from "react";
import Axios from "axios";
import * as API_CONSTANTS from "../../Common/APIConstants";
import { Grid, Segment, GridRow, Header, Menu } from "semantic-ui-react";
import ServiceCategoryItem from "./ServiceCategoryItem";
import { Template } from "../../Common/HelperComponents/Template";

class ServiceCategories extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      categories_info: "",
      services_info: "",
      activeIndex: 0,
      render_panes: false
    };
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
            categories_info: categories_info,
            category: categories_info[0],
            activeItem: categories_info[0].name
          });
        }.bind(this)
      )
      .catch(error => console.log(error));
  }

  handleItemClick = category => {
    this.setState({ category: category, activeItem: category.name });
    console.log(category);
  };

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
    const { activeItem, category } = this.state;
    return (
      <Grid>
        <GridRow>
          <Grid.Column width={5}>
            <Segment basic>
              <Menu fluid vertical tabular>
                {categories
                  ? categories.map(
                      function(category, i) {
                        return (
                          <Menu.Item
                            key={i}
                            name={category.name}
                            active={activeItem === category.name}
                            onClick={() => this.handleItemClick(category)}
                          >
                            <Header as="h4">{category.name}</Header>
                          </Menu.Item>
                        );
                      }.bind(this)
                    )
                  : "Loading"}
              </Menu>
            </Segment>
          </Grid.Column>

          <Grid.Column stretched width={11}>
            <Segment basic>
              <div className="Categories">
                <Segment basic>
                  <Grid>
                    <GridRow>
                      <Header as="h2" color="brown">
                        {category ? category.name : "Loading"}
                      </Header>
                    </GridRow>
                    <GridRow>
                      <Header as="h3">
                        {category ? category.short_desc : "Loading"}
                      </Header>
                    </GridRow>
                    <GridRow>
                      <Header as="h5">
                        {category ? (
                          <Template>{category.long_desc}</Template>
                        ) : (
                          "Loading"
                        )}
                      </Header>
                    </GridRow>
                  </Grid>
                </Segment>
              </div>
            </Segment>
          </Grid.Column>
        </GridRow>
        <GridRow>
          <Segment basic>
            {category
              ? services.map(function(service, i) {
                  if (category.name === service.category) {
                    return (
                      <ServiceCategoryItem key={i} serviceItem={service} />
                    );
                  } else {
                    return "";
                  }
                })
              : "Loading"}
          </Segment>
        </GridRow>
      </Grid>
    );
  }
}

export default ServiceCategories;
