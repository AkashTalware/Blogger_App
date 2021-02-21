import React from 'react'
import {connect} from 'react-redux'
import {SiFacebook, SiInstagram, SiTwitter, SiYoutube} from 'react-icons/si'
import {Row, Col} from 'react-bootstrap'

class Footer extends React.Component{
    render(){
        return(
            <div>
                <footer className="m-auto">
                    <h4>Follow Us on</h4>
                    <Row className="m-auto">
                        <Col sm = {{ span: 1 }} offset = {{span: 1}}><SiFacebook/></Col>
                        <Col sm = {{ span: 1 }} offset = {{span: 1}}><SiInstagram/></Col>
                        <Col sm = {{ span: 1 }} offset = {{span: 1}}><SiTwitter/></Col>
                        <Col sm = {{ span: 1 }} offset = {{span: 1}}><SiYoutube/></Col>
                    </Row>
                </footer>
            </div>
        )
    }
}

export default connect()(Footer)