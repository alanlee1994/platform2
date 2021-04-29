import React, { Component } from 'react';
import { Menu, Segment} from 'semantic-ui-react';


export default class NavBar extends Component {
    state = { activeItem: 'home' }
  
    handleItemClick = (e, { name }) => this.setState({ activeItem: name })
  
    render() {
      const { activeItem } = this.state
  
      return (
        <Segment inverted>
          <Menu inverted secondary>
            <Menu.Item
              name='Legend Signal Platform'
              active={activeItem === 'home'}
              onClick={this.handleItemClick}
            />
          </Menu>
          
        </Segment>
      )
    }
  }

