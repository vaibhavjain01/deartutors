/* eslint-env node, es6 */
import React from "react";
import Axios from "axios";
import * as API_CONSTANTS from "../../Common/APIConstants";
import { Grid, Segment, GridRow, Header } from "semantic-ui-react";

class PresenceMap extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hours_info: "None" };
  }

  componentDidMount() {
    const header = {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("JWTAccess")
      }
    };
    Axios.get(API_CONSTANTS.API_HOURS_OF_OPERATION, header)
      .then(
        function(response) {
          const hours_info = response.data.map(c => {
            return {
              id: c.id,
              day: c.day,
              start_time: c.start_time,
              end_time: c.end_time
            };
          });

          this.setState({
            hours_info: hours_info
          });
        }.bind(this)
      )
      .catch(error => console.log(error));
  }

  render() {
    const { hours_info } = this.state;

    const days = [];
    const start_times = [];
    const end_times = [];
    const day_times = [];

    for (var i = 0; i < hours_info.length; i++) {
      days.push(hours_info[i]["day"]);
      start_times.push(hours_info[i]["start_time"]);
      end_times.push(hours_info[i]["end_time"]);
      day_times.push(
        hours_info[i]["day"] +
          ": " +
          hours_info[i]["start_time"] +
          "-" +
          hours_info[i]["end_time"]
      );
    }

    return (
      <div className="Hours">
        <Segment basic>
          <Grid textAlign="center">
            <GridRow>
              <Header as="h1">Hours of Operations</Header>
            </GridRow>
            {day_times.map(function(day_time) {
              return (
                <GridRow textAlign="center">
                  <Header as="h4">{day_time}</Header>
                </GridRow>
              );
            })}
          </Grid>
        </Segment>
      </div>
    );
  }
}

export default PresenceMap;
