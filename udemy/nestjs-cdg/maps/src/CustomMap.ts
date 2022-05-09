export interface Mappable {
    color: string
    location: {
        lat: number
        lng: number
    }
    markerContent(): string
}

export class CustomMap {
    private googleMap: google.maps.Map

    constructor(divMap: string) {
        this.googleMap =  new google.maps.Map(document.getElementById(divMap),
            {
                zoom: 0,
                center: {
                    lat: 0,
                    lng: 0 
                }
            }
        )
    }

    addMarker(mappable: Mappable) {
        const marker = new google.maps.Marker({
            map: this.googleMap,
            position: mappable.location
        })

        marker.addListener('click', () => {
            const info = new google.maps.InfoWindow({
                content: mappable.markerContent()
            })
            info.open(this.googleMap, marker)
        })
    }
}