import { Controller, Get} from "@nestjs/common"

@Controller('/app')
class AppController {
    @Get()
    getRootRoute() {
        return "hi there!"
    }

    @Get("/bye")
    getBye() {
        return "Bye there!"
    }

}

export default AppController