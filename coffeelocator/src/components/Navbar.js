import { Link } from "react-router-dom";
import { NavLink } from "react-router-dom";
import './Navbar.css';

export default function Navbar() {

    return (
    <nav className="navbar">
        <NavLink to="/" className="navlinkhome" style={({ isActive }) => ({ 
            color: isActive ? "#ffffff" : "",
            fontWeight: isActive ? "bold" : "" })}>Coffee Stop</NavLink>
        
        <NavLink to="/coffeevendors" className="navlink" style={({ isActive }) => ({ 
            color: isActive ? "#ffffff" : "" ,
            fontWeight: isActive ? "bold" : ""})}>CoffeeMap</NavLink> 

        <NavLink to="/articles" className="navlink" style={({ isActive }) => ({ 
            color: isActive ? "#ffffff" : "" ,
            fontWeight: isActive ? "bold" : ""})}>Articles</NavLink>

        <NavLink to="/admin" className="navlink" style={({ isActive }) => ({ 
            color: isActive ? "#ffffff" : "" ,
            fontWeight: isActive ? "bold" : ""})}>Admin</NavLink> 
    </nav>
    )
}



