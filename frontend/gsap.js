import { gsap } from "gsap";
import { ScrambleTextPlugin } from "gsap/ScrambleTextPlugin";
gsap.registerPlugin(ScrambleTextPlugin);

gsap.to("#quote", { rotation: 27, x: 100, duration: 1 });