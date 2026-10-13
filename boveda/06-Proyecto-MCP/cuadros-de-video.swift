import AVFoundation
import AppKit
let url = URL(fileURLWithPath: CommandLine.arguments[1])
let out = CommandLine.arguments[2]
let paso = Double(CommandLine.arguments[3]) ?? 1.0
let asset = AVURLAsset(url: url)
let dur = CMTimeGetSeconds(asset.duration)
print("duracion", dur)
let gen = AVAssetImageGenerator(asset: asset)
gen.appliesPreferredTrackTransform = true
gen.requestedTimeToleranceBefore = .zero
gen.requestedTimeToleranceAfter = .zero
gen.maximumSize = CGSize(width: 480, height: 270)
var t = 0.0
var i = 0
while t < dur {
    if let cg = try? gen.copyCGImage(at: CMTime(seconds: t, preferredTimescale: 600), actualTime: nil) {
        let rep = NSBitmapImageRep(cgImage: cg)
        if let d = rep.representation(using: .png, properties: [:]) {
            try? d.write(to: URL(fileURLWithPath: String(format: "%@/c%04d.png", out, i)))
        }
    }
    t += paso; i += 1
}
print("cuadros", i)
