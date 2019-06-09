import React, { Component } from "react";
import { Divider, Tab } from "semantic-ui-react";
import * as COLORS from "../Common/ColorConstants";
import ServiceHome from "../ContentPages/ServiceHome/ServiceHome";
import ServiceCategories from "../ContentPages/ServiceCategories/ServiceCategories";
import ContactUs from "../ContentPages/ContactUs/ContactUs";
import AboutUs from "../ContentPages/AboutUs/AboutUs";

class ServiceMenu extends Component {
  state = { color: COLORS.COLOR_BLACK, content_color: COLORS.COLOR_VIOLET };
  render() {
    const menu_bg_color = "violet"; //this.props.menu_bg_color;
    const panes = [
      {
        menuItem: "Services",
        render: () => (
          <Tab.Pane attached={false}>
            <ServiceCategories />
          </Tab.Pane>
        )
      },
      {
        menuItem: "Contact",
        render: () => (
          <Tab.Pane attached={false}>
            <ContactUs />
          </Tab.Pane>
        )
      },
      {
        menuItem: "About",
        render: () => (
          <Tab.Pane attached={false}>
            <AboutUs />
          </Tab.Pane>
        )
      }
    ];

    return (
      <div className="ServiceMenu">
        <Divider hidden />
        <Tab
          menu={{
            color: menu_bg_color,
            inverted: true,
            attached: false,
            tabular: false
          }}
          panes={panes}
        />
      </div>
    );
  }
}

export default ServiceMenu;
