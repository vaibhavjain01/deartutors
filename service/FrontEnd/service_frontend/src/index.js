/* eslint-env node, es6 */
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import "semantic-ui-css/semantic.min.css";
import ServiceHeader from "./ServiceHeader/ServiceHeader";
import ServiceMenu from "./ServiceMenu/ServiceMenu";
import * as serviceWorker from "./serviceWorker";
import { Grid, GridColumn, Segment } from "semantic-ui-react";

function App() {
  const header_bg_color = "grey";
  const menu_bg_color = "teal";
  const max_grid_col_width = 10;
  return (
    <div className="App">
      <Grid>
        <GridColumn width="3" />
        <GridColumn width="10">
          <Segment color="teal" inverted>
            <ServiceHeader
              header_bg_color={header_bg_color}
              max_grid_col_width={max_grid_col_width}
            />
            <ServiceMenu menu_bg_color={menu_bg_color} />
          </Segment>
        </GridColumn>
        <GridColumn width="3" />
      </Grid>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
