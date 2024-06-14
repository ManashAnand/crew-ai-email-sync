
import { supabase } from "@/lib/supabaseClient";
import { NextRequest, NextResponse } from "next/server";
import axios from 'axios'

export async function GET(req, res) {
  try {
    // console.log(supabase)
    // const { data, error } = await supabase.from('emails').select()
    // console.log(data)

    // if (error) {
    //     console.log(error.message)
    //     return NextResponse.json(
    //         { msg: "Database goes down", success: false },
    //         { status: 501 }
    //       );
    // }
    const {data} = await axios.get(`http://127.0.0.1:8000/emails`);
    // console.log(response)
    console.log(data)

    // return NextResponse.json({ data }, { status: 200 });
    return NextResponse.json(
        { msg: "API is healthy", success: true ,data},
        { status: 200 }
      );
  } catch (error) {
    console.log(error);
    return NextResponse.json(
      { msg: "Database goes down from backend", success: false },
      { status: 501 }
    );
  }
}