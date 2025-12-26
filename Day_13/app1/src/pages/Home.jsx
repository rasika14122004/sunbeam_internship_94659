import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import { getAllStationery } from "../services/stationeryService";

// functionl component
export default function Home() {

    const [items, setItems] = useState([])

    // It is used to work with lifecycle of the component
    useEffect(() => {
        console.log('Home component loaded')
        getProducts()
    }, []) // compulsary pass the dependency array as empty

    const getProducts = async () => {
        const result = await getAllStationery()
        if (result.status == "success") {
            setItems(result.data)
        }

    }

    return <>
        <Navbar />
        <div className="container">
            <div className="row">
                {items.map(e => {
                    return <div className="mt-3 col-4">
                        <div className="card" style={{ width: "20rem" }}>
                            <div className="card-body">
                                <h5 className="card-title" style={{ height: "2rem" }}>{e.name}</h5>
                                <h6 className="card-subtitle mb-2 text-body-secondary">{e.brand}</h6>
                                <p className="card-text" style={{ height: "3rem" }}>{e.description}</p>
                                <h6 className="card-subtitle mb-2 text-body-secondary">Rs. {e.price}</h6>
                                <button className="btn btn-primary">Add to cart</button>
                            </div>
                        </div>
                    </div>
                })}
            </div>
        </div>

    </>
}
