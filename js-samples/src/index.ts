/*
 * Copyright 2019 Google LLC. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/* eslint-disable no-undef, @typescript-eslint/no-unused-vars, no-unused-vars */
import "./style.css";

import * as dotenv from 'dotenv';

var map_arr = [] as any;
var win_arr = [] as any;

function initMap() {
  const myLatlng = { lat: 46.5196535, lng: 6.6322734 };

  let range = [0,1,2,3,4,5,6,7,8,9];

  for (let i of range) {
    let id = 'map' + i.toString()
    console.log(id)
    let map = new google.maps.Map(document.getElementById(id)!, {
      zoom: 4,
      center: myLatlng,
      streetViewControl: false,
      fullscreenControl: false,
    });

    // Create the initial InfoWindow.
    let infoWindow = new google.maps.InfoWindow({
      content: JSON.stringify(myLatlng, null, 2),
      position: myLatlng,
    });

    infoWindow.open(map);

    // Configure the click listener.
    map.addListener("click", (mapsMouseEvent) => {
      // Set new position
      infoWindow.setPosition(mapsMouseEvent.latLng)

      infoWindow.setContent(
        JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2)
      );
      infoWindow.open(map);
    });
    map_arr.push(map)
    win_arr.push(infoWindow)
  }
}

function submit() {
  console.log(win_arr[0].content)
  let team_name = (<HTMLInputElement>document.getElementById("name")).value;
  console.log(team_name)

  const fs = require('fs');

  const answer = {
    "team_name": team_name,
    "pos0": JSON.parse(win_arr[0].content),
    "pos1": JSON.parse(win_arr[1].content),
    "pos2": JSON.parse(win_arr[2].content),
    "pos3": JSON.parse(win_arr[3].content),
    "pos4": JSON.parse(win_arr[4].content),
    "pos5": JSON.parse(win_arr[5].content),
    "pos6": JSON.parse(win_arr[6].content),
    "pos7": JSON.parse(win_arr[7].content),
    "pos8": JSON.parse(win_arr[8].content),
    "pos9": JSON.parse(win_arr[9].content),
  }

  let data = JSON.stringify(answer, null, 2)
  console.log(data)
  let url = 'http://' + process.env.HOST_IP + ':5000/submit';
  console.log(url)
  //let url = "http://localhost:5000/submit";

  let xhr = new XMLHttpRequest();
  xhr.open("POST", url);

  xhr.setRequestHeader("Accept", "application/json");
  xhr.setRequestHeader("Content-Type", "application/json");

  xhr.onreadystatechange = function () {
     if (xhr.readyState === 4) {
        console.log(xhr.status);
        console.log(xhr.responseText);
     }};

  xhr.send(data);

  //document.getElementById("content")!.innerHTML = "<pre>"+data+"</pre>";
  //window.location.pathname = "/end.html"
  //let results = document.getElementById("result-after")!.innerHTML = "<pre>"+data+"</pre>"

  //window.open("end.html")
}
export { initMap, submit };
